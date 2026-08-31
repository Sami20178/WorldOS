window.WorldSettings = {
  theme: localStorage.getItem('worldos-theme') || 'dark',
  setTheme(theme) {
    this.theme = theme;
    localStorage.setItem('worldos-theme', theme);
    document.documentElement.dataset.theme = theme;
  }
};
