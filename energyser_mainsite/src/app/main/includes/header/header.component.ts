import { AfterViewInit, Component, OnInit, Renderer2 } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-header',
  imports: [RouterModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent implements OnInit, AfterViewInit {

  constructor(
    private renderer: Renderer2,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    // this.router.events.subscribe(event => {
    //   if (event instanceof NavigationEnd) {
    //     this.updateActiveLink();
    //   }
    // });
  }

  ngAfterViewInit(): void {
    // this.updateActiveLink(); 
  }

  // private updateActiveLink() {
  //   document.querySelectorAll('#navmenu a').forEach(link => {
  //     if (link instanceof HTMLAnchorElement) {
  //       const linkPath = link.getAttribute('href');
  //       const currentPath = this.router.url;

  //       if (linkPath && currentPath.includes(linkPath)) {
  //         link.classList.add('active');
  //       } else {
  //         link.classList.remove('active');
  //       }
  //     }
  //   });
  // }
  
}
