# findSingularForWit
Input a witness and a collation file location and find all variation units where the given witness has a singular reading.

In the terminal
1) navegate to the script's directory on the hard drive. I keep mine in the same directory as the collation file. This is not necessary as you can provide a location for the collation file when prompted.
2) enter ```python3 -m findSingularForWit``` N.B. You may need to leave the .py extention off for the script to run properly.
3) The script will prompt you to enter a witness, e.g., ```Please enter witnesses: 1735```
4) The script will then promot you to enter the location of your collation file. For me, this is just its name since the script and the collation are in the same directory. Note that the collation file should be a TEI compliant XML file.
   ```Please enter the path of the XML file: ecmCatFinal.xml```
5) The script will print out to the terminal each variation unit where the given witness has a singular reading. It will provide the vartiant address and the reading. My example comes from the ECM of Jude.
```
B26K1V5U12-20	None	None	d	απαξ τουτο οτι κυριος ιησους
B26K1V5U22-26	None	None	af2	εκ γης λαoν
B26K1V6U32-34	None	None	b	ημερας μεγαλης
B26K1V6U40-42	None	None	c	εις ζοφον
B26K1V18U8-14	None	None	p	επ εσχατων του χρονου ελευσονται
B26K1V21U24-30	None	None	c	ιησου εις ζωην
```

In the above example, the "None" in two columns after the variation unit address assumes a different format in the collation file. The above XML files looks like this:

```
<app n="B26K1V5U12-20">
  <rdg n="a" wit="A 03">υμας απαξ παντα οτι ιησους</rdg>
  <rdg n="b" wit="02 81 2344">απαξ παντα οτι ιησους</rdg>
  <rdg n="c" type="singular" wit="33">απαξ παντα οτι ο ιησους</rdg>
</app>
```

A different collation file format might provide a from="" to="" for the variation unit address. For example, B26K1V5U12-20 means "Book 26" (Jude), K1 (Chapter 1), V5 (Verse 5), U12-20 (variation unit 12-20, referring to the words in squence in the text. This is based on how the ECM numbers words in the main text). Some collations may not use the U12-20, but rather provide the address in the code as such: from="12" to="20". For example:

```
<app n="Jude5" type="main"
      from="12" to="22">
      <rdg wit="03 NA28" varSeq="1" n="a" type="substitution">υμας απαξ παντα οτι ιησους</rdg>
      <rdg wit="02 81 2344" varSeq="2" n="b" type="mixed">απαξ παντα οτι ιησους</rdg>
      <rdg wit="33" varSeq="3" n="c" type="singular">απαξ παντα οτι ο ιησους</rdg>
</app>
```
In this case, the script works just the same, but provides the variation unit address as from and to where the "None"'s are printed above. For example:

```
me@me bin % python3 -m findSingularForWit
Please enter witnesses: 1735
Please enter the path of the XML file: JudeFinal20240404.xml
Jude5	12	22	d	απαξ τουτο οτι κυριος ιησους
Jude5	24	30	b	εκ γης λαον αιγυπτου
Jude18	10	16	o	επ εσχατων του χρονου ελευσονται
Jude18	22	32	hr1	τας επιθυμιας αυτων πορευομενοι των ασεβηων
```
