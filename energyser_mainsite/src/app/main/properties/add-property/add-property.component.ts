import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormArray, FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

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
    private http: HttpClient, 
    private modalService: NgbModal
  ) {
      this.personalInfoForm = this.fb.group({
        email: ['', [Validators.required, Validators.email]],
        typeClient: ['', Validators.required],
        adresse: ['', Validators.required]
      });
  
      this.propertyForm = this.fb.group({
        propertyType: ['', Validators.required],
        propertyName: ['', Validators.required],
        devices: this.fb.array([])
        });
    }

  

  ngOnInit(): void {
    
  }

  get devices(): FormArray {
    return this.propertyForm.get('devices') as FormArray;
  }

  addDevice(deviceData: any) {
    const device = this.fb.group({
      name: [deviceData.name, Validators.required],
      power: [deviceData.power, [Validators.required, Validators.min(0)]],
      usageTime: [deviceData.usageTime, [Validators.required, Validators.min(0)]],
      usagePeriod: [deviceData.usagePeriod, Validators.required]
    });
    this.devices.push(device);
  }

  submitForm() {
    if (this.personalInfoForm.valid && this.propertyForm.valid) {
      const formData = {
        personalInfo: this.personalInfoForm.value,
        property: this.propertyForm.value
      };
      console.log('Form Data:', formData);
    } else {
      alert('Please fill out all fields correctly.');
    }
  }
  
}
