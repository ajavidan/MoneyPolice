import { AppComponent } from './app.component';
import { AppModule } from './app.module';

import { enableProdMode } from '@angular/core';

import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';



platformBrowserDynamic().bootstrapModule(AppModule);

enableProdMode();
