# WhatsApp Anti-Link Bot

A simple WhatsApp anti-link bot using whatsapp-web.js. It monitors group messages and removes messages containing links (if the bot is an admin). Non-admin senders are warned.

## Requirements

- Node.js 14+ (recommended 16+)
- Chrome/Chromium installed (used by puppeteer)
- A terminal to scan QR code with your phone

## Setup

1. Copy the files into a folder:
   - package.json
   - index.js
   - antilink.js
   - .gitignore

2. Install dependencies:
```bash
npm install
```

3. Start the bot:
```bash
npm start
```

4. Scan the QR code shown in the terminal with WhatsApp on your phone.

## Important Notes

- To delete messages for everyone the bot must be a group admin.
- The session is stored automatically in `.wwebjs_auth`. Don't commit it to the repo (it's in .gitignore).
- For debugging, set `puppeteer.headless` to `false` in `index.js` to watch the browser.

## Customization

- Adjust `linkRegex` in `antilink.js` to change what counts as a link.
- Add per-group toggles or commands (e.g., enable/disable antilink) by storing group settings and checking them in `handleMessage`.

## Next steps / Enhancements

- Add commands to enable/disable anti-link per group.
- Store group preferences in a simple JSON or database.
- Add logging or admin-only override commands.
