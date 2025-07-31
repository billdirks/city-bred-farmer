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
            if (link.href && link.href.includes(currentPage)) {
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