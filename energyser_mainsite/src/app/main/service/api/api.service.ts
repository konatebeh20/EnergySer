import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  // private apiUrl = 'http://localhost:5000/api/add-property';

  apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }
  
  // addProperty(formData: any): Observable<any> {
  //   return this.http.post(this.apiUrl, formData);
  // }

  // EnergyConsoumption(formData: any): Observable<any> {
  //   return this.http.post(this.apiUrl, formData);
  // }
  
  CreateProperties(body:any) {
    return this.http.post(this.apiUrl + "api/properties/add-property", body)
  }

}
