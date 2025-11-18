const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const antilink = require('./antilink');

const client = new Client({
  authStrategy: new LocalAuth(), // stores session in .wwebjs_auth
  puppeteer: { headless: true } // change to false during debugging to see browser
});

client.on('qr', (qr) => {
  console.log('Scan this QR with WhatsApp:');
  qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
  console.log('WhatsApp client is ready!');
});

client.on('message', async (message) => {
  try {
    await antilink.handleMessage(client, message);
  } catch (err) {
    console.error('Error handling message:', err);
  }
});

client.initialize();
