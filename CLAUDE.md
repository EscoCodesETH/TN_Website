# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a static marketing website for True Numbers, a blockchain defense solutions company. The site is built with vanilla HTML, CSS, and JavaScript - no frameworks or build tools required.

## Development Commands
Since this is a static site with no build process:
- **Run locally**: Open `index.html` directly in a web browser
- **Test changes**: Refresh the browser after editing files
- **Deploy**: Push to GitHub Pages or upload files to any static hosting service

## Architecture
The codebase follows a simple, flat structure:
- `index.html` - Single page containing all content sections
- `styles.css` - All styling, organized by component with responsive breakpoints
- `script.js` - Minimal functionality (form handler, intersection observer)
- `images/` - All image assets

## Key Technical Details
- **Design System**: Miami Vice color scheme (pink #FF00FF, cyan #00FFFF) with dark theme
- **Responsive Breakpoints**: 1200px, 900px, 768px, 500px
- **CSS Architecture**: Component-based organization with BEM-like naming
- **JavaScript**: ES6, no dependencies, progressive enhancement approach
- **Form Handling**: Currently shows alert only - no backend integration

## Common Tasks
- **Update content**: Edit sections directly in `index.html`
- **Modify styles**: Find component in `styles.css` (sections are clearly commented)
- **Add images**: Place in `images/` folder and reference in HTML/CSS
- **Test responsive design**: Use browser developer tools device emulation