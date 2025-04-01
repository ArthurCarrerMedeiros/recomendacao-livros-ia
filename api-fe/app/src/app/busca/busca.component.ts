import { Component } from '@angular/core';
import { BuscaService } from './busca.service';

@Component({
  selector: 'app-busca',
  standalone: false,
  templateUrl: './busca.component.html',
  styleUrl: './busca.component.css',
})
export class BuscaComponent {
  pesquisa: string = '';

  constructor(private buscaService: BuscaService) {}

  async listarRecomendacoes() {
    try {
      const resposta = await this.buscaService.listarRecomendacoes(
        this.pesquisa
      );
      console.log(resposta);
    } catch (error) {
      console.log(error);
    }
  }
}
