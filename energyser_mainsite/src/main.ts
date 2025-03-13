import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';


// Declare external libraries
declare var PureCounter: any;
declare var AOS: any;
declare var GLightbox: any;
declare var Waypoint: any;
declare var imagesLoaded: any;
declare var Isotope: any;
declare var Swiper: any;

bootstrapApplication(AppComponent, appConfig)
  .then(() => {
    // Initialize BizLand after Angular app is loaded
    document.addEventListener('DOMContentLoaded', () => {
      const bizland = new BizLandInit();
      bizland.init();
    });
  })
  .catch((err) => console.error(err));


/**
 * BizLand Template functionality class
 */

class BizLandInit {
  private mobileNavToggleBtn: HTMLElement | null;
  private scrollTop: HTMLElement | null;

  constructor() {
    this.mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');
    this.scrollTop = document.querySelector('.scroll-top');
  }

  /**
   * Initialize all BizLand template features
   */
  public init(): void {
    this.setupScrollEvents();
    this.setupMobileNav();
    this.setupDropdowns();
    this.removePreloader();
    this.setupScrollTop();
    this.initAOS();
    this.initGLightbox();
    this.initSkillsAnimation();
    this.initPureCounter();
    this.initSwiper();
    this.initIsotope();
    this.setupFAQToggles();
    this.correctScrollPosition();
    this.setupNavmenuScrollspy();
  }

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  private toggleScrolled(): void {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    
    if (!selectHeader?.classList.contains('scroll-up-sticky') && 
        !selectHeader?.classList.contains('sticky-top') && 
        !selectHeader?.classList.contains('fixed-top')) return;
    
    if (selectBody) {
      window.scrollY > 100 
        ? selectBody.classList.add('scrolled') 
        : selectBody.classList.remove('scrolled');
    }
  }

  /**
   * Setup scroll event listeners
   */
  private setupScrollEvents(): void {
    document.addEventListener('scroll', () => this.toggleScrolled());
    window.addEventListener('load', () => this.toggleScrolled());
  }

  /**
   * Mobile nav toggle functionality
   */
  private mobileNavToogle(): void {
    const body = document.querySelector('body');
    body?.classList.toggle('mobile-nav-active');
    this.mobileNavToggleBtn?.classList.toggle('bi-list');
    this.mobileNavToggleBtn?.classList.toggle('bi-x');
  }

  /**
   * Setup mobile navigation
   */
  private setupMobileNav(): void {
    if (this.mobileNavToggleBtn) {
      this.mobileNavToggleBtn.addEventListener('click', () => this.mobileNavToogle());
    }

    // Hide mobile nav on same-page/hash links
    document.querySelectorAll('#navmenu a').forEach(navmenu => {
      navmenu.addEventListener('click', () => {
        if (document.querySelector('.mobile-nav-active')) {
          this.mobileNavToogle();
        }
      });
    });
  }

  /**
   * Toggle mobile nav dropdowns
   */
  private setupDropdowns(): void {
    document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
      // Use arrow function to preserve 'this' context
      navmenu.addEventListener('click', (e) => {
        e.preventDefault();
        
        // Fix: Safely cast to Element type and access DOM properties
        const element = e.currentTarget as Element;
        const parentElement = element.parentElement;
        
        if (parentElement) {
          parentElement.classList.toggle('active');
          const nextSibling = parentElement.nextElementSibling as Element;
          if (nextSibling) {
            nextSibling.classList.toggle('dropdown-active');
          }
        }
        
        e.stopImmediatePropagation();
      });
    });
  }

  /**
   * Remove preloader
   */
  private removePreloader(): void {
    const preloader = document.querySelector('#preloader');
    if (preloader) {
      window.addEventListener('load', () => {
        preloader.remove();
      });
    }
  }

  /**
   * Toggle scroll top button visibility
   */
  private toggleScrollTop(): void {
    if (this.scrollTop) {
      window.scrollY > 100 
        ? this.scrollTop.classList.add('active') 
        : this.scrollTop.classList.remove('active');
    }
  }

  /**
   * Setup scroll top button
   */
  private setupScrollTop(): void {
    if (this.scrollTop) {
      this.scrollTop.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });

      window.addEventListener('load', () => this.toggleScrollTop());
      document.addEventListener('scroll', () => this.toggleScrollTop());
    }
  }

  /**
   * Initialize AOS (Animation On Scroll)
   */
  private initAOS(): void {
    window.addEventListener('load', () => {
      AOS.init({
        duration: 600,
        easing: 'ease-in-out',
        once: true,
        mirror: false
      });
    });
  }

  /**
   * Initialize GLightbox
   */
  private initGLightbox(): void {
    const glightbox = GLightbox({
      selector: '.glightbox'
    });
  }

  /**
   * Animate the skills items on reveal
   */
  private initSkillsAnimation(): void {
    const skillsAnimation = document.querySelectorAll('.skills-animation');
    skillsAnimation.forEach((item) => {
      new Waypoint({
        element: item,
        offset: '80%',
        handler: function(direction: string) {
          const progress = item.querySelectorAll('.progress .progress-bar');
          progress.forEach(el => {
            (el as HTMLElement).style.width = el.getAttribute('aria-valuenow') + '%';
          });
        }
      });
    });
  }

  /**
   * Initialize Pure Counter
   */
  private initPureCounter(): void {
    new PureCounter();
  }

  /**
   * Initialize Swiper sliders
   */
  private initSwiper(): void {
    window.addEventListener("load", () => {
      document.querySelectorAll(".init-swiper").forEach((swiperElement) => {
        const configElement = swiperElement.querySelector(".swiper-config");
        if (!configElement) return;
        
        const config = JSON.parse(configElement.innerHTML.trim());

        if (swiperElement.classList.contains("swiper-tab")) {
          this.initSwiperWithCustomPagination(swiperElement as HTMLElement, config);
        } else {
          // Using declared Swiper
          new Swiper(swiperElement, config);
        }
      });
    });
  }

  /**
   * Initialize Swiper with custom pagination
   */
  private initSwiperWithCustomPagination(swiperElement: HTMLElement, config: any): void {
    // You would need to implement this method if needed
    console.warn('initSwiperWithCustomPagination not implemented');
  }

  /**
   * Initialize Isotope layout and filters
   */
  private initIsotope(): void {
    document.querySelectorAll('.isotope-layout').forEach((isotopeItem) => {
      const layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
      const filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
      const sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

      const container = isotopeItem.querySelector('.isotope-container');
      if (!container) return;

      let initIsotope: any;
      imagesLoaded(container, function() {
        initIsotope = new Isotope(container, {
          itemSelector: '.isotope-item',
          layoutMode: layout,
          filter: filter,
          sortBy: sort
        });
      });

      isotopeItem.querySelectorAll('.isotope-filters li').forEach((filters) => {
        // Use arrow function to preserve 'this' context
        filters.addEventListener('click', (e) => {
          const clickedElement = e.currentTarget as Element;
          const activeFilter = isotopeItem.querySelector('.isotope-filters .filter-active');
          
          if (activeFilter) {
            activeFilter.classList.remove('filter-active');
          }
          
          clickedElement.classList.add('filter-active');
          
          const filterValue = clickedElement.getAttribute('data-filter');
          if (initIsotope && filterValue) {
            initIsotope.arrange({
              filter: filterValue
            });
          }
          
          if (typeof AOS !== 'undefined') {
            AOS.refresh();
          }
        }, false);
      });
    });
  }

  /**
   * Setup FAQ item toggles
   */
  private setupFAQToggles(): void {
    document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
      faqItem.addEventListener('click', () => {
        const parentElement = faqItem.parentElement;
        if (parentElement) {
          parentElement.classList.toggle('faq-active');
        }
      });
    });
  }

  /**
   * Correct scrolling position upon page load for URLs containing hash links
   */
  private correctScrollPosition(): void {
    window.addEventListener('load', () => {
      if (window.location.hash) {
        if (document.querySelector(window.location.hash)) {
          setTimeout(() => {
            const section = document.querySelector(window.location.hash) as HTMLElement;
            if (!section) return;
            
            const computedStyle = getComputedStyle(section);
            const scrollMarginTop = computedStyle.scrollMarginTop;
            
            window.scrollTo({
              top: section.offsetTop - parseInt(scrollMarginTop || '0'),
              behavior: 'smooth'
            });
          }, 100);
        }
      }
    });
  }

  /**
   * Setup Navmenu Scrollspy
   */
  private setupNavmenuScrollspy(): void {
    const navmenulinks = document.querySelectorAll('.navmenu a');

    const navmenuScrollspy = (): void => {
      navmenulinks.forEach(navmenulink => {
        // Fix: Use getAttribute('href') instead of hash
        const hash = navmenulink.getAttribute('href');
        if (!hash || !hash.startsWith('#')) return;
        
        const section = document.querySelector(hash) as HTMLElement;
        if (!section) return;
        
        const position = window.scrollY + 200;
        
        if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
          document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
          navmenulink.classList.add('active');
        } else {
          navmenulink.classList.remove('active');
        }
      });
    };

    window.addEventListener('load', navmenuScrollspy);
    document.addEventListener('scroll', navmenuScrollspy);
  }
}