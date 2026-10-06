"""Dependency-free content, navigation and performance checks for this static site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('index.html', 'stars/index.html')

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.tags = []
        self.text = []
        self.ids = []
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs: self.ids.append(attrs['id'])
    def handle_data(self, data):
        self.text.append(data)
    def all(self, tag):
        return [attrs for name, attrs in self.tags if name == tag]
    def content(self):
        return re.sub(r'\s+', ' ', ' '.join(self.text)).strip()
    def resolve(self, url):
        path = unquote(urlparse(url).path)
        return ROOT / path.lstrip('/') if path.startswith('/') else self.path.parent / path

class SiteContract(unittest.TestCase):
    def setUp(self):
        self.pages = [Page(ROOT / p) for p in PAGES if (ROOT / p).exists()]

    def test_both_product_routes_exist(self):
        for path in PAGES:
            self.assertTrue((ROOT / path).is_file(), f'missing required product page: {path}')

    def test_requested_product_copy_and_status(self):
        self.assertTrue('Clarity across military pay, personnel and travel.' in Page(ROOT / 'index.html').content(), 'UP³ product headline missing')
        self.assertTrue('UP³ is an Air Force pay, personnel and travel platform in development, combining rule-based entitlement evaluation with traceable regulatory citations and review workflows.' in Page(ROOT / 'index.html').content(), 'UP³ product description missing')
        stars = ROOT / 'stars/index.html'
        self.assertTrue(stars.exists(), 'STARS page has not been implemented')
        self.assertIn('Travel and reimbursement within UP³.', Page(stars).content())
        for page in self.pages:
            self.assertIn('In development · Demo available', page.content())
            self.assertIn('Built by True Numbers', page.content())
            self.assertRegex(page.content().lower(), r'synthetic')

    def test_demo_links_and_navigation(self):
        for page in self.pages:
            self.assertEqual(len(page.all('nav')), 1)
            anchors = page.all('a')
            self.assertTrue(any(a.get('href') == '/' for a in anchors), 'UP³ route link missing')
            self.assertTrue(any(a.get('href') == '/stars' for a in anchors), 'STARS route link missing')
            self.assertGreaterEqual(sum(a.get('href') == 'mailto:info@truenumbers.tech' for a in anchors), 2, 'demo CTA needed in navigation and content')
            self.assertNotIn('Explore the demo', page.content(), 'no valid public demo URL supplied')

    def test_no_company_contact_or_unsupported_marketing(self):
        for page in self.pages:
            self.assertEqual(page.all('form'), [], 'no contact/demo form is allowed')
            self.assertNotRegex(page.content(), r'(?i)blockchain|AI-driven|strategic partnerships|innovation partner|operationally deployed|accredited')
            for identifier in page.ids:
                self.assertNotRegex(identifier, r'(?i)company|about|contact')
            for anchor in page.all('a'):
                self.assertNotRegex(anchor.get('href',''), r'(?i)(?:^|/|#)(company|about|contact)(?:[/.#]|$)')

    def test_accessible_landmarks_and_local_links(self):
        for page in self.pages:
            self.assertEqual(len(page.all('h1')), 1)
            self.assertEqual(len(page.all('main')), 1)
            self.assertEqual(len(page.all('footer')), 1)
            self.assertEqual(len(page.ids), len(set(page.ids)), 'duplicate IDs')
            self.assertTrue(any(a.get('href') == '#main' for a in page.all('a')), 'skip link missing')
            self.assertTrue(any(x.get('name') == 'viewport' for x in page.all('meta')))
            for anchor in page.all('a'):
                href = anchor.get('href', '')
                if href.startswith('#'):
                    self.assertIn(href[1:], page.ids)
                elif href and not urlparse(href).scheme:
                    resolved = page.resolve(href)
                    self.assertTrue(resolved.is_file() or (resolved / 'index.html').is_file(), f'broken local link: {href}')

    def test_product_illustrations_are_described(self):
        for page in self.pages:
            visuals = [a for tag,a in page.tags if a.get('role') == 'img'] + page.all('img')
            self.assertGreaterEqual(len(visuals), 1, 'product visual missing')
            self.assertIsNotNone(re.search(r'(?i)illustrati(?:on|ve).*synthetic|synthetic.*illustrati(?:on|ve)', page.content()), 'illustrations must be labeled')
            for visual in visuals:
                self.assertGreaterEqual(len(visual.get('alt', visual.get('aria-label',''))), 20)
            for image in page.all('img'):
                self.assertGreater(int(image.get('width', '0')), 0)
                self.assertGreater(int(image.get('height', '0')), 0)
                self.assertTrue(page.resolve(image['src']).is_file())

    def test_media_budget_and_loading(self):
        for page in self.pages:
            images = page.all('img')
            self.assertLessEqual(sum(i.get('loading') != 'lazy' for i in images), 1)
            media = {page.resolve(i['src']) for i in images}
            self.assertLessEqual(sum(p.stat().st_size for p in media), 600_000, 'page media budget is 600 kB')
            for p in media:
                self.assertLessEqual(p.stat().st_size, 250_000, f'image exceeds 250 kB: {p.name}')
            for tag in ('script', 'link'):
                for asset in page.all(tag):
                    url = asset.get('src', asset.get('href',''))
                    self.assertNotRegex(url, r'^https?://', 'no external render-blocking fonts or runtime')

    def test_no_continuous_animation_or_scroll_work(self):
        css = (ROOT / 'styles.css').read_text()
        scripts = [p.read_text() for p in ROOT.glob('*.js')]
        self.assertIsNone(re.search(r'(?i)animation\s*:[^;]*\binfinite\b|background-attachment\s*:\s*fixed|backdrop-filter', css), 'continuous animation, fixed backgrounds or backdrop blur still present')
        for script in scripts:
            self.assertNotRegex(script, r"addEventListener\(\s*['\"]scroll['\"]")
        self.assertIn('prefers-reduced-motion', css)

    def test_travel_payment_boundary_is_explicit(self):
        stars = ROOT / 'stars/index.html'
        self.assertTrue(stars.exists(), 'STARS page has not been implemented')
        content = Page(stars).content().lower()
        for term in ('authorization', 'voucher', 'finance review', 'payment', 'joint travel regulations'):
            self.assertIn(term, content)
        self.assertRegex(content, r'(actual|external) payment')
        self.assertRegex(content, r'planned|in development')

    def test_sidebar_labels_have_readable_contrast(self):
        css = (ROOT / 'styles.css').read_text()
        def color(selector, property_name):
            rule = re.search(re.escape(selector) + r'\s*\{([^}]+)\}', css)
            self.assertIsNotNone(rule, f'missing style for {selector}')
            value = re.search(r'(?<![-\w])' + property_name + r'\s*:\s*(#[0-9a-fA-F]{6})', rule.group(1))
            self.assertIsNotNone(value, f'missing explicit {property_name} for {selector}')
            return value.group(1)
        def luminance(hex_color):
            channels = [int(hex_color[i:i+2], 16)/255 for i in (1,3,5)]
            linear = [c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4 for c in channels]
            return sum(c*w for c,w in zip(linear, (0.2126,0.7152,0.0722)))
        background = luminance(color('.window-sidebar', 'background'))
        for selector in ('.sidebar-label', '.sidebar-bottom span'):
            with self.subTest(selector=selector):
                foreground = luminance(color(selector, 'color'))
                ratio = (max(foreground,background)+0.05)/(min(foreground,background)+0.05)
                self.assertGreaterEqual(ratio, 4.5, f'{selector} contrast {ratio:.2f}:1 is below 4.5:1')

if __name__ == '__main__':
    unittest.main(verbosity=2)
