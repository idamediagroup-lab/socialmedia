/**
 * CREDIT SCRIPTS — bulk CTA update
 * Replaces every comment/DM call-to-action with:  Comment "SCORE" to learn more
 *
 * HOW TO RUN
 *  1. script.google.com  →  New project  →  paste this file in
 *  2. Run  dryRun()  first. Nothing is changed. Read the log (View → Logs).
 *  3. When the log looks right, run  applyChanges().
 *
 * Authorise when prompted — it only touches this one folder.
 */

var FOLDER_ID = '1tFVZXcmZull85ZZX2YwgRMcwP8wPbRY9';   // CREDIT SCRIPTS
var NEW_CTA   = 'Comment "SCORE" to learn more';

/**
 * Ordered most-specific first. Each entry replaces the whole CTA sentence.
 * “” are curly quotes — the docs use both kinds.
 */
var PATTERNS = [
  // Comment "WORD" ...rest of sentence
  /(?:👇\s*)?\b[Cc]omment\s+(?:the\s+word\s+)?["“”']?[A-Z][A-Z0-9 ]{1,20}["“”']?[^.!?\n]*[.!?]?/g,
  /\bCOMMENT\s+(?:THE\s+WORD\s+)?["“”']?[A-Z][A-Z0-9 ]{1,20}["“”']?[^.!?\n]*[.!?]?/g,
  // DM the word "WORD" ...
  /\b[Dd][Mm]\s+(?:me\s+)?(?:the\s+word\s+)?["“”']?[A-Z][A-Z0-9 ]{1,20}["“”']?[^.!?\n]*[.!?]?/g
];

function dryRun()      { run_(true);  }
function applyChanges(){ run_(false); }

function run_(preview) {
  var files = DriveApp.getFolderById(FOLDER_ID).getFilesByType(MimeType.GOOGLE_DOCS);
  var scanned = 0, changed = 0, hits = 0, untouched = [];

  while (files.hasNext()) {
    var f = files.next();
    scanned++;
    var doc  = DocumentApp.openById(f.getId());
    var body = doc.getBody();
    var text = body.getText();
    var found = [];

    PATTERNS.forEach(function (re) {
      re.lastIndex = 0;
      var m;
      while ((m = re.exec(text)) !== null) {
        var s = m[0].trim();
        if (s && s.toUpperCase().indexOf('"SCORE"') === -1) found.push(s);
      }
    });

    if (!found.length) { untouched.push(f.getName()); continue; }

    Logger.log('── ' + f.getName());
    found.forEach(function (old) {
      Logger.log('    ' + old + '   →   ' + NEW_CTA);
      hits++;
      if (!preview) body.replaceText(escapeRe_(old), NEW_CTA);
    });

    if (!preview) doc.saveAndClose();
    changed++;
  }

  Logger.log('');
  Logger.log(preview ? '=== DRY RUN — nothing was changed ===' : '=== CHANGES APPLIED ===');
  Logger.log('Docs scanned:      ' + scanned);
  Logger.log('Docs with a CTA:   ' + changed);
  Logger.log('CTAs replaced:     ' + hits);
  Logger.log('Docs with NO CTA:  ' + untouched.length);
  untouched.forEach(function (n) { Logger.log('    (no CTA) ' + n); });
}

/** Escape a literal string for replaceText, which takes a regex. */
function escapeRe_(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
