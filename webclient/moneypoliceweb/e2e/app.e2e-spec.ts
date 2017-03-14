import { MoneypolicewebPage } from './app.po';

describe('moneypoliceweb App', () => {
  let page: MoneypolicewebPage;

  beforeEach(() => {
    page = new MoneypolicewebPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
