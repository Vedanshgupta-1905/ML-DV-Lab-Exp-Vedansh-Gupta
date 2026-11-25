# Experiment 2: Data Cleaning and Transformation

## Aim
Implement Data Cleaning and Transformation using Power BI Desktop.

## Dataset
[retail_dirty.csv](retail_dirty.csv) (synthetic demonstration data).

## Procedure
Open Transform data. Rename UnitPrice to Unit Price; set Date to Date, Quantity to whole number, Sales to decimal number. Replace null Region with Unknown; remove rows with null Sales; remove duplicate rows. Add custom column using `[Quantity] * [Unit Price]`. Close & Apply. Power Query M examples: `Table.ReplaceValue(Source,null,"Unknown",Replacer.ReplaceValue,{"Region"})` and `Table.Distinct(PreviousStep)` (replace step names as needed).

## Expected result
The configured visual or transformation should demonstrate the stated aim. Save your Power BI report and add a screenshot of your actual output after completing the procedure.
