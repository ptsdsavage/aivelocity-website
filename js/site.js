/**
 * AI Velocity Fund — Site JavaScript
 * Stealth Institutional · Minimal Runtime
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    loadComponents().then(function () {
      initMobileNav();
      initDropdowns();
      initSmoothScroll();
    });
  });

  /**
   * Load Navigation and Footer Components
   */
  function loadComponents() {
    var promises = [];

    var navPlaceholder = document.getElementById('nav-placeholder');
    var footerPlaceholder = document.getElementById('footer-placeholder');

    if (navPlaceholder) {
      promises.push(
        fetch('/components/navigation.html')
          .then(function (res) { return res.text(); })
          .then(function (html) { navPlaceholder.innerHTML = html; })
          .catch(function () { /* silently fail */ })
      );
    }

    if (footerPlaceholder) {
      promises.push(
        fetch('/components/footer.html')
          .then(function (res) { return res.text(); })
          .then(function (html) { footerPlaceholder.innerHTML = html; })
          .catch(function () { /* silently fail */ })
      );
    }

    return Promise.all(promises);
  }

  /**
   * Mobile Navigation Toggle
   */
  function initMobileNav() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (!navToggle || !navMenu) return;

    navToggle.addEventListener('click', function () {
      navMenu.classList.toggle('active');
      const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', !isExpanded);
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.navbar')) {
        navMenu.classList.remove('active');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    });

    // Close mobile menu when clicking a nav-link (not dropdown toggle)
    const navLinks = navMenu.querySelectorAll('.nav-link');
    navLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth <= 768) {
          navMenu.classList.remove('active');
          navToggle.setAttribute('aria-expanded', 'false');
        }
      });
    });
  }

  /**
   * Dropdown Menu Functionality
   */
  function initDropdowns() {
    const dropdownToggles = document.querySelectorAll('.nav-dropdown-toggle');

    dropdownToggles.forEach(function (toggle) {
      toggle.addEventListener('click', function (e) {
        e.preventDefault();
        const isExpanded = this.getAttribute('aria-expanded') === 'true';

        // On mobile, close other dropdowns
        if (window.innerWidth <= 768) {
          dropdownToggles.forEach(function (t) {
            if (t !== toggle) {
              t.setAttribute('aria-expanded', 'false');
            }
          });
        }

        this.setAttribute('aria-expanded', !isExpanded);
      });
    });

    // Close dropdowns when clicking outside (desktop)
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.nav-dropdown')) {
        dropdownToggles.forEach(function (toggle) {
          toggle.setAttribute('aria-expanded', 'false');
        });
      }
    });
  }

  /**
   * Smooth Scroll for Anchor Links
   */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
  }

})();
