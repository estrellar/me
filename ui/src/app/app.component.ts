import { Component, OnInit } from '@angular/core';
import { RestApiService } from './services/rest-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'Me';
  me: any = [];

  constructor(public restApi: RestApiService){}

  ngOnInit(){
    this.getMe();
  }

  getMe(){
    return this.restApi.getMe().subscribe((data: {}) =>{
       this.me = data;
     });
  }
}
