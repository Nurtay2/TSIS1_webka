import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HomeComponent } from "./home/home.component";
import { AboutComponent } from './about/about.component';
import { AlbumPhotosComponent } from './album-photos/album-photos.component';
import { AlbumsComponent } from './albums/albums.component';
import { AlbumsDetailComponent } from './albums-detail/albums-detail.component';
import { TopBarComponent } from './top-bar/top-bar.component';

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
    imports: [RouterOutlet, HomeComponent, TopBarComponent, AboutComponent, AlbumPhotosComponent, AlbumsComponent, AlbumsDetailComponent]
})
export class AppComponent {
  title = 'Album';
}
