import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { TransferComponent } from './transfer/transfer.component';
import { FundComponent } from './funds/funds.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    TransferComponent,
    FundComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent, HeaderComponent, TransferComponent, FundComponent]
})
export class AppModule { }
