import { Component } from '@angular/core';

@Component({
  selector: 'fund',
  templateUrl: './funds.component.html',
  styleUrls: ['./funds.component.scss']
})

export class FundComponent {

  fundName: string = 'Food';
  fundLimit: number = 100;
  fundCurrentAmount: number = 50;
  fundNewAmount: number = 0;

}
