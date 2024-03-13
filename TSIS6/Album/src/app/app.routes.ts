import { Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';
import { AlbumsComponent } from './albums/albums.component';
import { AlbumsDetailComponent } from './albums-detail/albums-detail.component';

export const routes: Routes = [
    {path:'', component: HomeComponent, title: "Home"},
    {path:'home', component: HomeComponent, title: "Home"},
    {path:'about', component: AboutComponent, title: "About"},
    {path:'albums', component: AlbumsComponent, title: "Albums"},
    {path:'albums/:id', component: AlbumsDetailComponent, title: "Albums-Details"},
];
