import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { PostService } from '../post.service';
import { Album } from '../albums';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-albums-detail',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './albums-detail.component.html',
  styleUrl: './albums-detail.component.css'
})
export class AlbumsDetailComponent implements OnInit{
  title: '';
  Ialbum: Album = {} as Album;


  constructor(private activateRoute: ActivatedRoute, private postService: PostService){
    this.title = '';
  }

  ngOnInit(): void {
    const id = this.activateRoute.snapshot.paramMap.get('id')!;
    this.postService.getPost(+id).subscribe((Ialbum) => {
      this.Ialbum = Ialbum;
    });
    }

}
