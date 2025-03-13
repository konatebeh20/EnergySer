import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HeaderComponent } from "./includes/header/header.component";
import { FooterComponent } from "./includes/footer/footer.component";

declare var AOS: any;
declare var GLightbox: any;
declare var imagesLoaded: any;
declare var Isotope: any;
declare var Swiper: any;


@Component({
  selector: 'app-main',
  imports: [RouterModule, HeaderComponent, FooterComponent],
  templateUrl: './main.component.html',
  styleUrl: './main.component.scss'
})
export class MainComponent {

}
