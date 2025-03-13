import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PropertiesComponent } from './properties.component';
import { AddPropertyComponent } from './add-property/add-property.component';
import { PropertiesDetailsComponent } from './properties-details/properties-details.component';
import { RecommendationComponent } from './recommendation/recommendation.component';

const routes: Routes = [
  {path:"",component:PropertiesComponent,
      children:[
        { path: '', redirectTo: 'login', pathMatch: 'full' },
        { path: 'add-property', component: AddPropertyComponent },
        { path: 'property-details', component: PropertiesDetailsComponent },
        { path: 'recommendation', component: RecommendationComponent },
       
      ]
    }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PropertiesRoutingModule { }
