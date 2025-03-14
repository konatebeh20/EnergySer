import { Component, OnInit } from '@angular/core';

import {  FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

import { CommonModule } from '@angular/common';
import { ApiService } from '../../service/api/api.service';


declare var bootstrap: any;


@Component({
  selector: 'app-add-property',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './add-property.component.html',
  styleUrls: ['./add-property.component.scss']
})
export class AddPropertyComponent implements OnInit {

  isloading: boolean = false;

  properties_form: FormGroup = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    type_client: new FormControl('Particulier', Validators.required),
    adresse: new FormControl('', Validators.required),
    property_type: new FormControl('House', Validators.required),
    property_name: new FormControl('', Validators.required),

    global_active_power: new FormControl('', Validators.required),
    global_reactive_power: new FormControl('', Validators.required),
    voltage: new FormControl('', Validators.required),
    global_intensity: new FormControl('', Validators.required),
    sub_metering_1: new FormControl('', Validators.required),
    sub_metering_2: new FormControl('', Validators.required),
    sub_metering_3: new FormControl('', Validators.required),
  })

  ApiService: any;


  constructor(

    private api: ApiService,
  ) {
    this.isloading = false;
   }


  ngOnInit(): void {}

  sendProperties() {
    this.isloading = true;
    console.log("Hi This is Properties data:", this.properties_form.value)

    this.api.CreateProperties(this.properties_form.value).subscribe({
          next:(res:any)=> {
            console.log("Message sent successfully :", res);
            // this.showSuccessToast("Your message has been successfully sent!");
            this.properties_form.reset();

            this.isloading = false;
          },
          error: (err: any) => {
            console.log("Error while sending :", err);
            // this.showErrorToast("Message failed to send. Please try again.");

            this.isloading = false;
          },
          complete: () => {
            this.isloading = false;
            // console.log("contactService match");
          },
    })

  };

  showSuccessToast(message: string) {
    const toastBody = document.getElementById("successToastBody");
    if (toastBody) {
      toastBody.textContent = message;
    } else {
      console.warn("Success toast body element not found.");
    }

    const toastElement = document.getElementById("successToast");
    const toast = new bootstrap.Toast(toastElement, { delay: 2000 });
    toast.show();
  }

  showErrorToast(message: string) {
    const toastBody = document.getElementById("errorToastBody");
    if (toastBody) {
      toastBody.textContent = message;
    } else {
      console.warn("Error toast body element not found.");
    }

    const toastElement = document.getElementById("errorToast");
    const toast = new bootstrap.Toast(toastElement, { delay: 2000 });
    toast.show();
  }

}
