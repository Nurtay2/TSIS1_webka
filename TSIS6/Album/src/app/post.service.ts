import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Album} from "./albums"

@Injectable({
  providedIn: 'root'
})

export class PostService{
  BASE_URL: string = 'https://jsonplaceholder.typicode.com'
  constructor(private http: HttpClient) {
  }
  getPosts(): Observable<Album[]>{
    return this.http.get<Album[]>(`${this.BASE_URL}/posts`);
  }
  createPost(newPost: Album): Observable<Album> {
    return this.http.post<Album>(`${this.BASE_URL}/posts`, newPost);
  }
  getPost(id: number): Observable<Album> {
    return this.http.get<Album>(`${this.BASE_URL}/posts/${id}`);
  }
  deletePost(id: number) {
    return this.http.delete(`${this.BASE_URL}/posts/${id}`);
  }
}
