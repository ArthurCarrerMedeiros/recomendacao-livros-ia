import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BuscaComponent } from './busca/busca.component';

const routes: Routes = [{ path: '', component: BuscaComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
