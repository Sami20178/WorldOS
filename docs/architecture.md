# World OS Architecture

World OS is split into shared core logic and platform-specific interfaces.

## Layers
1. Core — system state, settings and application registry.
2. Shared — configuration and visual tokens.
3. Desktop — mouse/keyboard-oriented interface.
4. Mobile — touch-oriented phone/tablet interface.
5. Apps — built-in World OS applications.

The web prototype is intentionally lightweight so it can later become a base for native desktop and Android/tablet builds.
