import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
// import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormArray, FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ApiService } from '../../service/api/api.service';

@Component({
  selector: 'app-add-property',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './add-property.component.html',
  styleUrls: ['./add-property.component.scss']
})
export class AddPropertyComponent implements OnInit {
 
  personalInfoForm: FormGroup;
  propertyForm: FormGroup;
  
  constructor(
    private fb: FormBuilder,
    private rf: ReactiveFormsModule,
    private http: HttpClient,
    private apiService: ApiService,
    // private modalService: NgbModal
  ) {
    this.personalInfoForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      typeClient: ['', Validators.required],
      adresse: ['', Validators.required]
    });

    this.propertyForm = this.fb.group({
      propertyType: ['', Validators.required],
      propertyName: ['', Validators.required],
      devices: this.fb.array([])  // Example of adding a FormArray
    });
  }

  ngOnInit(): void {
    
  }
  
}
