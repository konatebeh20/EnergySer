import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './main.component';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { ServicePageComponent } from './service-page/service-page.component';

const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
      { path: '', redirectTo: 'home', pathMatch: 'full'},
      { path: 'home', component: HomeComponent },
      { path: 'about', component: AboutComponent },
      { path: 'services', component: ServicePageComponent },
      { path: 'auth', loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule) },
      { path: 'properties', loadChildren: () => import('./properties/properties.module').then(m => m.PropertiesModule) },
      // { path: 'features', component: FeaturesComponent },
      // { path: 'contact-us', component: ContactUsComponent },
      // { path: 'register', component: RegisterComponent },
      // { path: 'sitemap', component: SitemapComponent },
      // { path: 'policies/privacy', component: PrivacyComponent },
      // { path: 'policies/terms', component: TermsComponent }

    ]
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }
