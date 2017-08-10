import { OndeVouPage } from './app.po';

describe('onde-vou App', function() {
  let page: OndeVouPage;

  beforeEach(() => {
    page = new OndeVouPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
