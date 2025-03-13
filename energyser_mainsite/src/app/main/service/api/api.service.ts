import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://localhost:5000/api/add-property';

  constructor(private http: HttpClient) { }
  
  addProperty(formData: any): Observable<any> {
    return this.http.post(this.apiUrl, formData);
  }
  
}
