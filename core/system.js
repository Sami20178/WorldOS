window.WorldSystem = {
  openWindows: new Map(),
  openApp(id) {
    const app = window.WORLD_OS.apps.find(a => a.id === id);
    if (!app) return;
    this.openWindows.set(id, app);
    window.dispatchEvent(new CustomEvent('worldos:open', { detail: app }));
  },
  closeApp(id) {
    this.openWindows.delete(id);
    window.dispatchEvent(new CustomEvent('worldos:close', { detail: { id } }));
  },
  toggleApp(id) {
    this.openWindows.has(id) ? this.closeApp(id) : this.openApp(id);
  }
};
