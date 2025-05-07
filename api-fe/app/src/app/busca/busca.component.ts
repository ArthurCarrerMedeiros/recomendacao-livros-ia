import { Component } from '@angular/core';
import { BuscaService } from './busca.service';
import { LivroModel } from '../models/livro.model';
import { ListagemLivrosComponent } from '../listagem-livros/listagem-livros.component';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-busca',
  standalone: false,
  templateUrl: './busca.component.html',
  styleUrl: './busca.component.css',
})
export class BuscaComponent {
  pesquisa: string = '';
  carregando: boolean = false;

  constructor(private buscaService: BuscaService, private dialog: MatDialog) {}

  async listarRecomendacoes() {
    this.carregando = true;
    try {
      const resposta: LivroModel[] =
        await this.buscaService.listarRecomendacoes(this.pesquisa);
      this.abrirDialog(resposta);
    } catch (error) {
      console.log(error);
    } finally {
      this.carregando = false;
    }
  }

  private abrirDialog(livros: LivroModel[]) {
    this.dialog.open(ListagemLivrosComponent, {
      data: {
        listaLivrosRecomendados: livros,
      },
      width: '80%',
    });
  }
}
