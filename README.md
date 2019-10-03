# discarddup
compares two files line per lines and removes duplicate on the second one

./discarddup file_for_testing file_for_writing

the first argument is a file that will be left untouched, the second argument is a file for which we'll erase the lines already present on the first file.

DO NOT USE WITH HUGE FILES, use https://github.com/nil0x42/duplicut instead
