import { NgModule } from '@angular/core';
import {
  BrowserModule,
  provideClientHydration,
  withEventReplay,
} from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BuscaComponent } from './busca/busca.component';
import {
  HttpClientModule,
  provideHttpClient,
  withFetch,
} from '@angular/common/http';

@NgModule({
  declarations: [AppComponent, BuscaComponent],
  imports: [BrowserModule, AppRoutingModule, HttpClientModule, FormsModule],
  providers: [
    provideHttpClient(withFetch()),
    provideClientHydration(withEventReplay()),
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
