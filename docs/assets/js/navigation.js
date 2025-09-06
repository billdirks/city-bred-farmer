// Navigation script to preserve sidebar scroll position
(function() {
    'use strict';
    
    // Store the current page URL to identify which page we're on
    const currentPage = window.location.pathname;
    
    // Function to save sidebar scroll position to sessionStorage
    function saveSidebarScroll() {
        const sidebar = document.querySelector('.sidebar');
        if (sidebar) {
            sessionStorage.setItem('sidebarScrollPosition', sidebar.scrollTop);
        }
    }
    
    // Function to restore sidebar scroll position from sessionStorage
    function restoreSidebarScroll() {
        const sidebar = document.querySelector('.sidebar');
        if (sidebar) {
            const savedPosition = sessionStorage.getItem('sidebarScrollPosition');
            if (savedPosition !== null) {
                sidebar.scrollTop = parseInt(savedPosition);
            }
        }
    }

    // Ensure selected link is visible inside the sidebar without unnecessary scrolling
    function ensureSelectedVisible() {
        const sidebar = document.querySelector('.sidebar');
        if (!sidebar) return;
        const selected = sidebar.querySelector('nav a.selected');
        if (!selected) return;
        const sidebarRect = sidebar.getBoundingClientRect();
        const selectedRect = selected.getBoundingClientRect();
        const padding = 2; // small tolerance for borders/subpixel

        // If selected is above, align to start; if below, align to end
        if (selectedRect.top < sidebarRect.top + padding) {
            selected.scrollIntoView({ block: 'start' });
        } else if (selectedRect.bottom > sidebarRect.bottom - padding) {
            selected.scrollIntoView({ block: 'end' });
        }
    }
    
    // Function to handle navigation clicks
    function handleNavigationClick(event) {
        const link = event.target.closest('a');
        if (link && link.href && !link.href.includes('#')) {
            // Save current scroll position before navigation
            saveSidebarScroll();
            
            // Add a small delay to ensure the scroll position is saved
            setTimeout(() => {
                window.location.href = link.href;
            }, 10);
        }
    }
    
    // Function to highlight the current page in navigation
    function highlightCurrentPage() {
        const navLinks = document.querySelectorAll('.sidebar nav a');
        navLinks.forEach(link => {
            // Extract the pathname from the link href
            const linkPath = new URL(link.href, window.location.origin).pathname;
            
            if (linkPath === currentPage) {
                link.classList.remove('unselected');
                link.classList.add('selected');
            } else {
                link.classList.remove('selected');
                link.classList.add('unselected');
            }
        });
    }
    
    // Initialize when DOM is loaded
    document.addEventListener('DOMContentLoaded', function() {
        // Restore scroll position
        restoreSidebarScroll();
        
        // Highlight current page
        highlightCurrentPage();

        // Make sure the selected item is visible if near edges
        ensureSelectedVisible();
        
        // Add click event listeners to navigation links
        const sidebar = document.querySelector('.sidebar');
        if (sidebar) {
            sidebar.addEventListener('click', handleNavigationClick);
        }
        
        // Save scroll position when user scrolls the sidebar
        sidebar.addEventListener('scroll', function() {
            saveSidebarScroll();
        });
    });
    
    // Save scroll position before page unload
    window.addEventListener('beforeunload', saveSidebarScroll);
    
})(); 