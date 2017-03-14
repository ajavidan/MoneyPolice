import { Routes } from '@angular/router';
import { Component1Component } from './component1.component';
import { Component2Component } from './component2.component';

export const appRoutes: Routes = [
  { path: '', redirectTo: '/component1', pathMatch: 'full'},
  { path: 'component1', component: Component1Component },
  { path: 'component2', component: Component2Component },
];
