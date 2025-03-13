import { Routes } from '@angular/router';
import { NotfoundComponent } from './main/notfound/notfound.component';

export const routes: Routes = [
  { path: '', redirectTo: '/main', pathMatch: 'full' },
  { path: 'main', loadChildren: () => import('./main/main.module').then(m => m.MainModule) },
  { path: '**', component: NotfoundComponent },
];
