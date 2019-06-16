/** 
from https://www.bettercloud.com/monitor/the-academy/extract-urls-or-link-text-from-a-google-sheets-cell/
 * Returns the URL of a hyperlinked cell, if it's entered with hyperlink command. 
 * Supports ranges
 * @param {A1}  reference Cell reference
 * @customfunction
 */
function linkURL(reference) {
  var sheet = SpreadsheetApp.getActiveSheet();
  var formula = SpreadsheetApp.getActiveRange().getFormula();
  var args = formula.match(/=\w+\((.*)\)/i);
  try {
    var range = sheet.getRange(args[1]);
  }
  catch(e) {
    throw new Error(args[1] + ' is not a valid range');
  }
  var formulas = range.getFormulas();
  var output = [];
  for (var i = 0; i < formulas.length; i++) {
    var row = [];
    for (var j = 0; j < formulas[0].length; j++) {
      var url = formulas[i][j].match(/=hyperlink\("([^"]+)"/i);
      row.push(url ? url[1] : '');
    }
    output.push(row);
  }
  return output
}
