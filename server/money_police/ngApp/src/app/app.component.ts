import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
  template: `<h1>Hello {{name}}</h1>
            <nav>
              <a routerLink="/component1" routerLinkActive="active">1</a>
              <a routerLink="/component2" routerLinkActive="active">2</a>
            </nav>
            <router-outlet></router-outlet>

  `,
})

export class AppComponent  { name = 'Money Police'; }
