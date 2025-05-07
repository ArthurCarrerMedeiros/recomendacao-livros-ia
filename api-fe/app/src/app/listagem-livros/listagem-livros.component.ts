import { Component, OnInit, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { LivroModel } from '../models/livro.model';

@Component({
  selector: 'app-listagem-livros',
  standalone: false,
  templateUrl: './listagem-livros.component.html',
  styleUrls: ['./listagem-livros.component.css'],
})
export class ListagemLivrosComponent implements OnInit {
  listaLivrosRecomendados: LivroModel[] = [];

  constructor(
    @Inject(MAT_DIALOG_DATA)
    public modalData: { listaLivrosRecomendados: LivroModel[] }
  ) {}

  ngOnInit() {
    this.listaLivrosRecomendados = this.modalData.listaLivrosRecomendados || [];
  }
}
