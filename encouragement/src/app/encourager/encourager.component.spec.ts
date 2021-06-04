import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EncouragerComponent } from './encourager.component';

describe('EncouragerComponent', () => {
  let component: EncouragerComponent;
  let fixture: ComponentFixture<EncouragerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EncouragerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EncouragerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
