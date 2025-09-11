# Overview

This is a personal portfolio website for Utsav Pal, a Computer Science student at VIT Bhopal University. The portfolio showcases his background as a Python developer specializing in AI, Machine Learning, and Full Stack Development. The website features an About Me section highlighting his education and technical expertise, a Projects section displaying key work including an Advanced Ecommerce Recommendation System, Handwritten Digit Recognition, Predictive Health Diagnosis System, and Face Recognition System. The site serves as a professional showcase of his skills in Python, NLP, TensorFlow, OpenCV, and Flask, with a focus on AI and data-driven solutions.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
The portfolio uses a simple static website architecture built with vanilla HTML, CSS, and JavaScript. The main page (`index.html`) implements a single-page design using Tailwind CSS for styling and responsive layout. The design features a dark mode theme by default with smooth transitions and hover effects for interactivity. The layout uses CSS Grid for the projects section to create a responsive card-based display that adapts to different screen sizes (mobile, tablet, desktop).

## Backend Architecture
The project includes a minimal Python-based HTTP server (`server.py`) designed specifically for the Replit environment. The server extends Python's built-in `SimpleHTTPRequestHandler` to serve static files with appropriate caching headers for development purposes. It's configured to run on `0.0.0.0:5000` to work with Replit's proxy system and includes environment variable support for flexible port configuration during deployment.

## Styling and UI Framework
The frontend leverages Tailwind CSS via CDN for rapid styling and responsive design. Custom CSS is minimal and focuses on theme transitions and font family definitions. The color scheme uses a dark theme with gray-800 backgrounds and accent colors for interactive elements like buttons and project cards.

# External Dependencies

## CDN Dependencies
- **Tailwind CSS**: Loaded via CDN (`https://cdn.tailwindcss.com`) for utility-first CSS framework and responsive design components

## Python Standard Library
- **http.server**: Used for creating the development HTTP server
- **socketserver**: Provides the TCP server implementation
- **os**: Handles environment variables and file system operations

## Deployment Platform
- **Replit**: The server configuration is specifically optimized for Replit's hosting environment with appropriate host binding and port configuration