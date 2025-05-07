import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { lastValueFrom } from 'rxjs';
import { LivroModel } from '../models/livro.model';

@Injectable({
  providedIn: 'root',
})
export class BuscaService {
  private backendUrl = environment.backendUrl;

  constructor(private http: HttpClient) {}

  async listarRecomendacoes(pesquisa: string): Promise<LivroModel[]> {
    const params = new HttpParams().set('mensagem', pesquisa);
    try {
      return await lastValueFrom(
        this.http.get<LivroModel[]>(`${this.backendUrl}/livros`, { params })
      );
    } catch (error) {
      throw error;
    }
  }
}
