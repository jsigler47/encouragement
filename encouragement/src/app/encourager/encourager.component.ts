import { Component, OnInit } from '@angular/core';
import { data } from '../data';

@Component({
  selector: 'app-encourager',
  templateUrl: './encourager.component.html',
  styleUrls: ['./encourager.component.scss']
})
export class EncouragerComponent implements OnInit {
  getStatement = this.randomNoRepeats(data);
  activeStatement: string = "";

  constructor() {
  }

  ngOnInit(): void {
    this.activeStatement = this.getStatement();
  }

  getNewStatement() {
    this.activeStatement = this.getStatement();
  }

  randomNoRepeats(array: string []) {
    var copy = array.slice(0);
    return function() {
      if (copy.length < 1) { copy = array.slice(0); }
      var index = Math.floor(Math.random() * copy.length);
      var item = copy[index];
      copy.splice(index, 1);
      return item;
    };
  }

}
