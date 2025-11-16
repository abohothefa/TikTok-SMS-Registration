# إعداد Cursor لاستخدام OpenRouter API

## الخطوات:

### الطريقة 1: عبر واجهة الإعدادات
1. افتح Cursor
2. اضغط `Ctrl + ,` (أو `Cmd + ,` على Mac) لفتح الإعدادات
3. ابحث عن "OpenRouter" أو "API Key"
4. أدخل مفتاح OpenRouter الخاص بك

### الطريقة 2: عبر ملف الإعدادات JSON
1. اضغط `Ctrl + Shift + P` (أو `Cmd + Shift + P` على Mac)
2. اكتب: `Preferences: Open User Settings (JSON)`
3. أضف الإعدادات التالية:

```json
{
  "cursor.ai.apiKey": "YOUR_OPENROUTER_API_KEY_HERE",
  "cursor.ai.provider": "openrouter"
}
```

أو إذا كان Cursor يستخدم إعدادات مختلفة:

```json
{
  "openrouter.apiKey": "YOUR_OPENROUTER_API_KEY_HERE"
}
```

### الطريقة 3: عبر متغيرات البيئة
أضف المفتاح إلى ملف `~/.bashrc` أو `~/.zshrc`:

```bash
export OPENROUTER_API_KEY="YOUR_OPENROUTER_API_KEY_HERE"
```

ثم أعد تشغيل Terminal أو نفذ:
```bash
source ~/.bashrc
```

## الحصول على المفتاح:
1. اذهب إلى: https://openrouter.ai/settings/credits
2. انسخ مفتاح API الخاص بك
3. الصقه في الإعدادات أعلاه

## ملاحظات:
- تأكد من استبدال `YOUR_OPENROUTER_API_KEY_HERE` بمفتاحك الفعلي
- قد تحتاج لإعادة تشغيل Cursor بعد التعديل
- تحقق من أن لديك رصيد كافٍ في OpenRouter
