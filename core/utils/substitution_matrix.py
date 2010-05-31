#!/usr/bin/python
# Filename: substitution_matrix.py

# Substitution matrix information
# from http://portal.open-bio.org/pipermail/biopython/2000-September/000418.html
# ---
# This code is part of the Trait-o-matic project and is governed by its license.

blosum = {
	95 : {
		('A', 'A') : 5, ('A', 'R') : -2, ('A', 'N') : -2, ('A', 'D') : -3, 
		('A', 'C') : -1, ('A', 'Q') : -1, ('A', 'E') : -1, ('A', 'G') : -1, 
		('A', 'H') : -3, ('A', 'I') : -2, ('A', 'L') : -2, ('A', 'K') : -1, 
		('A', 'M') : -2, ('A', 'F') : -3, ('A', 'P') : -1, ('A', 'S') : 1, 
		('A', 'T') : 0, ('A', 'W') : -4, ('A', 'Y') : -3, ('A', 'V') : -1, 
		('A', 'B') : -3, ('A', 'Z') : -1, ('A', 'X') : -1, 
		('R', 'R') : 7, ('R', 'N') : -1, ('R', 'D') : -3, ('R', 'C') : -5, 
		('R', 'Q') : 0, ('R', 'E') : -1, ('R', 'G') : -4, ('R', 'H') : -1, 
		('R', 'I') : -4, ('R', 'L') : -3, ('R', 'K') : 2, ('R', 'M') : -2, 
		('R', 'F') : -4, ('R', 'P') : -3, ('R', 'S') : -2, ('R', 'T') : -2, 
		('R', 'W') : -4, ('R', 'Y') : -3, ('R', 'V') : -4, ('R', 'B') : -2, 
		('R', 'Z') : -1, ('R', 'X') : -2, 
		('N', 'N') : 7, ('N', 'D') : 1, ('N', 'C') : -4, ('N', 'Q') : 0, 
		('N', 'E') : -1, ('N', 'G') : -1, ('N', 'H') : 0, ('N', 'I') : -4, 
		('N', 'L') : -5, ('N', 'K') : 0, ('N', 'M') : -3, ('N', 'F') : -4, 
		('N', 'P') : -3, ('N', 'S') : 0, ('N', 'T') : -1, ('N', 'W') : -5, 
		('N', 'Y') : -3, ('N', 'V') : -4, ('N', 'B') : 4, ('N', 'Z') : -1, 
		('N', 'X') : -2, 
		('D', 'D') : 7, ('D', 'C') : -5, ('D', 'Q') : -1, ('D', 'E') : 1, 
		('D', 'G') : -2, ('D', 'H') : -2, ('D', 'I') : -5, ('D', 'L') : -5, 
		('D', 'K') : -2, ('D', 'M') : -5, ('D', 'F') : -5, ('D', 'P') : -3, 
		('D', 'S') : -1, ('D', 'T') : -2, ('D', 'W') : -6, ('D', 'Y') : -5, 
		('D', 'V') : -5, ('D', 'B') : 4, ('D', 'Z') : 0, ('D', 'X') : -2, 
		('C', 'C') : 9, ('C', 'Q') : -4, ('C', 'E') : -6, ('C', 'G') : -5, 
		('C', 'H') : -5, ('C', 'I') : -2, ('C', 'L') : -3, ('C', 'K') : -5, 
		('C', 'M') : -3, ('C', 'F') : -3, ('C', 'P') : -5, ('C', 'S') : -2, 
		('C', 'T') : -2, ('C', 'W') : -4, ('C', 'Y') : -4, ('C', 'V') : -2, 
		('C', 'B') : -4, ('C', 'Z') : -5, ('C', 'X') : -3, 
		('Q', 'Q') : 7, ('Q', 'E') : 2, ('Q', 'G') : -3, ('Q', 'H') : 1, 
		('Q', 'I') : -4, ('Q', 'L') : -3, ('Q', 'K') : 1, ('Q', 'M') : -1, 
		('Q', 'F') : -4, ('Q', 'P') : -2, ('Q', 'S') : -1, ('Q', 'T') : -1, 
		('Q', 'W') : -3, ('Q', 'Y') : -3, ('Q', 'V') : -3, ('Q', 'B') : -1, 
		('Q', 'Z') : 4, ('Q', 'X') : -1, 
		('E', 'E') : 6, ('E', 'G') : -3, ('E', 'H') : -1, ('E', 'I') : -4, 
		('E', 'L') : -4, ('E', 'K') : 0, ('E', 'M') : -3, ('E', 'F') : -5, 
		('E', 'P') : -2, ('E', 'S') : -1, ('E', 'T') : -2, ('E', 'W') : -5, 
		('E', 'Y') : -4, ('E', 'V') : -3, ('E', 'B') : 0, ('E', 'Z') : 4, 
		('E', 'X') : -2, 
		('G', 'G') : 6, ('G', 'H') : -3, ('G', 'I') : -6, ('G', 'L') : -5, 
		('G', 'K') : -3, ('G', 'M') : -4, ('G', 'F') : -5, ('G', 'P') : -4, 
		('G', 'S') : -1, ('G', 'T') : -3, ('G', 'W') : -5, ('G', 'Y') : -5, 
		('G', 'V') : -5, ('G', 'B') : -2, ('G', 'Z') : -3, ('G', 'X') : -3, 
		('H', 'H') : 9, ('H', 'I') : -4, ('H', 'L') : -4, ('H', 'K') : -1, 
		('H', 'M') : -3, ('H', 'F') : -2, ('H', 'P') : -3, ('H', 'S') : -2, 
		('H', 'T') : -2, ('H', 'W') : -3, ('H', 'Y') : 1, ('H', 'V') : -4, 
		('H', 'B') : -1, ('H', 'Z') : 0, ('H', 'X') : -2, 
		('I', 'I') : 5, ('I', 'L') : 1, ('I', 'K') : -4, ('I', 'M') : 1, 
		('I', 'F') : -1, ('I', 'P') : -4, ('I', 'S') : -3, ('I', 'T') : -2, 
		('I', 'W') : -4, ('I', 'Y') : -2, ('I', 'V') : 3, ('I', 'B') : -5, 
		('I', 'Z') : -4, ('I', 'X') : -2, 
		('L', 'L') : 5, ('L', 'K') : -3, ('L', 'M') : 2, ('L', 'F') : 0, 
		('L', 'P') : -4, ('L', 'S') : -3, ('L', 'T') : -2, ('L', 'W') : -3, 
		('L', 'Y') : -2, ('L', 'V') : 0, ('L', 'B') : -5, ('L', 'Z') : -4, 
		('L', 'X') : -2, 
		('K', 'K') : 6, ('K', 'M') : -2, ('K', 'F') : -4, ('K', 'P') : -2, 
		('K', 'S') : -1, ('K', 'T') : -1, ('K', 'W') : -5, ('K', 'Y') : -3, 
		('K', 'V') : -3, ('K', 'B') : -1, ('K', 'Z') : 0, ('K', 'X') : -1, 
		('M', 'M') : 7, ('M', 'F') : -1, ('M', 'P') : -3, ('M', 'S') : -3, 
		('M', 'T') : -1, ('M', 'W') : -2, ('M', 'Y') : -3, ('M', 'V') : 0, 
		('M', 'B') : -4, ('M', 'Z') : -2, ('M', 'X') : -2, 
		('F', 'F') : 7, ('F', 'P') : -5, ('F', 'S') : -3, ('F', 'T') : -3, 
		('F', 'W') : 0, ('F', 'Y') : 3, ('F', 'V') : -2, ('F', 'B') : -5, 
		('F', 'Z') : -4, ('F', 'X') : -2, 
		('P', 'P') : 8, ('P', 'S') : -2, ('P', 'T') : -2, ('P', 'W') : -5, 
		('P', 'Y') : -5, ('P', 'V') : -4, ('P', 'B') : -3, ('P', 'Z') : -2, 
		('P', 'X') : -3, 
		('S', 'S') : 5, ('S', 'T') : 1, ('S', 'W') : -4, ('S', 'Y') : -3, 
		('S', 'V') : -3, ('S', 'B') : -1, ('S', 'Z') : -1, ('S', 'X') : -1, 
		('T', 'T') : 6, ('T', 'W') : -4, ('T', 'Y') : -3, ('T', 'V') : -1, 
		('T', 'B') : -1, ('T', 'Z') : -2, ('T', 'X') : -1, 
		('W', 'W') : 11, ('W', 'Y') : 2, ('W', 'V') : -3, ('W', 'B') : -6, 
		('W', 'Z') : -4, ('W', 'X') : -4, 
		('Y', 'Y') : 8, ('Y', 'V') : -3, ('Y', 'B') : -4, ('Y', 'Z') : -4, 
		('Y', 'X') : -2, 
		('V', 'V') : 5, ('V', 'B') : -5, ('V', 'Z') : -3, ('V', 'X') : -2, 
		('B', 'B') : 4, ('B', 'Z') : 0, ('B', 'X') : -2, 
		('Z', 'Z') : 4, ('Z', 'X') : -1, 
		('X', 'X') : -2
	},
	100 : {
		('A', 'A') : 8, ('A', 'R') : -3, ('A', 'N') : -4, ('A', 'D') : -5, 
		('A', 'C') : -2, ('A', 'Q') : -2, ('A', 'E') : -3, ('A', 'G') : -1, 
		('A', 'H') : -4, ('A', 'I') : -4, ('A', 'L') : -4, ('A', 'K') : -2, 
		('A', 'M') : -3, ('A', 'F') : -5, ('A', 'P') : -2, ('A', 'S') : 1, 
		('A', 'T') : -1, ('A', 'W') : -6, ('A', 'Y') : -5, ('A', 'V') : -2, 
		('A', 'B') : -4, ('A', 'Z') : -2, ('A', 'X') : -2, 
		('R', 'R') : 10, ('R', 'N') : -2, ('R', 'D') : -5, ('R', 'C') : -8, 
		('R', 'Q') : 0, ('R', 'E') : -2, ('R', 'G') : -6, ('R', 'H') : -1, 
		('R', 'I') : -7, ('R', 'L') : -6, ('R', 'K') : 3, ('R', 'M') : -4, 
		('R', 'F') : -6, ('R', 'P') : -5, ('R', 'S') : -3, ('R', 'T') : -3, 
		('R', 'W') : -7, ('R', 'Y') : -5, ('R', 'V') : -6, ('R', 'B') : -4, 
		('R', 'Z') : -1, ('R', 'X') : -3, 
		('N', 'N') : 11, ('N', 'D') : 1, ('N', 'C') : -5, ('N', 'Q') : -1, 
		('N', 'E') : -2, ('N', 'G') : -2, ('N', 'H') : 0, ('N', 'I') : -7, 
		('N', 'L') : -7, ('N', 'K') : -1, ('N', 'M') : -5, ('N', 'F') : -7, 
		('N', 'P') : -5, ('N', 'S') : 0, ('N', 'T') : -1, ('N', 'W') : -8, 
		('N', 'Y') : -5, ('N', 'V') : -7, ('N', 'B') : 5, ('N', 'Z') : -2, 
		('N', 'X') : -3, 
		('D', 'D') : 10, ('D', 'C') : -8, ('D', 'Q') : -2, ('D', 'E') : 2, 
		('D', 'G') : -4, ('D', 'H') : -3, ('D', 'I') : -8, ('D', 'L') : -8, 
		('D', 'K') : -3, ('D', 'M') : -8, ('D', 'F') : -8, ('D', 'P') : -5, 
		('D', 'S') : -2, ('D', 'T') : -4, ('D', 'W') : -10, ('D', 'Y') : -7, 
		('D', 'V') : -8, ('D', 'B') : 6, ('D', 'Z') : 0, ('D', 'X') : -4, 
		('C', 'C') : 14, ('C', 'Q') : -7, ('C', 'E') : -9, ('C', 'G') : -7, 
		('C', 'H') : -8, ('C', 'I') : -3, ('C', 'L') : -5, ('C', 'K') : -8, 
		('C', 'M') : -4, ('C', 'F') : -4, ('C', 'P') : -8, ('C', 'S') : -3, 
		('C', 'T') : -3, ('C', 'W') : -7, ('C', 'Y') : -6, ('C', 'V') : -3, 
		('C', 'B') : -7, ('C', 'Z') : -8, ('C', 'X') : -5, 
		('Q', 'Q') : 11, ('Q', 'E') : 2, ('Q', 'G') : -5, ('Q', 'H') : 1, 
		('Q', 'I') : -6, ('Q', 'L') : -5, ('Q', 'K') : 2, ('Q', 'M') : -2, 
		('Q', 'F') : -6, ('Q', 'P') : -4, ('Q', 'S') : -2, ('Q', 'T') : -3, 
		('Q', 'W') : -5, ('Q', 'Y') : -4, ('Q', 'V') : -5, ('Q', 'B') : -2, 
		('Q', 'Z') : 5, ('Q', 'X') : -2, 
		('E', 'E') : 10, ('E', 'G') : -6, ('E', 'H') : -2, ('E', 'I') : -7, 
		('E', 'L') : -7, ('E', 'K') : 0, ('E', 'M') : -5, ('E', 'F') : -8, 
		('E', 'P') : -4, ('E', 'S') : -2, ('E', 'T') : -3, ('E', 'W') : -8, 
		('E', 'Y') : -7, ('E', 'V') : -5, ('E', 'B') : 0, ('E', 'Z') : 7, 
		('E', 'X') : -3, 
		('G', 'G') : 9, ('G', 'H') : -6, ('G', 'I') : -9, ('G', 'L') : -8, 
		('G', 'K') : -5, ('G', 'M') : -7, ('G', 'F') : -8, ('G', 'P') : -6, 
		('G', 'S') : -2, ('G', 'T') : -5, ('G', 'W') : -7, ('G', 'Y') : -8, 
		('G', 'V') : -8, ('G', 'B') : -3, ('G', 'Z') : -5, ('G', 'X') : -4, 
		('H', 'H') : 13, ('H', 'I') : -7, ('H', 'L') : -6, ('H', 'K') : -3, 
		('H', 'M') : -5, ('H', 'F') : -4, ('H', 'P') : -5, ('H', 'S') : -3, 
		('H', 'T') : -4, ('H', 'W') : -5, ('H', 'Y') : 1, ('H', 'V') : -7, 
		('H', 'B') : -2, ('H', 'Z') : -1, ('H', 'X') : -4, 
		('I', 'I') : 8, ('I', 'L') : 2, ('I', 'K') : -6, ('I', 'M') : 1, 
		('I', 'F') : -2, ('I', 'P') : -7, ('I', 'S') : -5, ('I', 'T') : -3, 
		('I', 'W') : -6, ('I', 'Y') : -4, ('I', 'V') : 4, ('I', 'B') : -8, 
		('I', 'Z') : -7, ('I', 'X') : -3, 
		('L', 'L') : 8, ('L', 'K') : -6, ('L', 'M') : 3, ('L', 'F') : 0, 
		('L', 'P') : -7, ('L', 'S') : -6, ('L', 'T') : -4, ('L', 'W') : -5, 
		('L', 'Y') : -4, ('L', 'V') : 0, ('L', 'B') : -8, ('L', 'Z') : -6, 
		('L', 'X') : -3, 
		('K', 'K') : 10, ('K', 'M') : -4, ('K', 'F') : -6, ('K', 'P') : -3, 
		('K', 'S') : -2, ('K', 'T') : -3, ('K', 'W') : -8, ('K', 'Y') : -5, 
		('K', 'V') : -5, ('K', 'B') : -2, ('K', 'Z') : 0, ('K', 'X') : -3, 
		('M', 'M') : 12, ('M', 'F') : -1, ('M', 'P') : -5, ('M', 'S') : -4, 
		('M', 'T') : -2, ('M', 'W') : -4, ('M', 'Y') : -5, ('M', 'V') : 0, 
		('M', 'B') : -7, ('M', 'Z') : -4, ('M', 'X') : -3, 
		('F', 'F') : 11, ('F', 'P') : -7, ('F', 'S') : -5, ('F', 'T') : -5, 
		('F', 'W') : 0, ('F', 'Y') : 4, ('F', 'V') : -3, ('F', 'B') : -7, 
		('F', 'Z') : -7, ('F', 'X') : -4, 
		('P', 'P') : 12, ('P', 'S') : -3, ('P', 'T') : -4, ('P', 'W') : -8, 
		('P', 'Y') : -7, ('P', 'V') : -6, ('P', 'B') : -5, ('P', 'Z') : -4, 
		('P', 'X') : -4, 
		('S', 'S') : 9, ('S', 'T') : 2, ('S', 'W') : -7, ('S', 'Y') : -5, 
		('S', 'V') : -4, ('S', 'B') : -1, ('S', 'Z') : -2, ('S', 'X') : -2, 
		('T', 'T') : 9, ('T', 'W') : -7, ('T', 'Y') : -5, ('T', 'V') : -1, 
		('T', 'B') : -2, ('T', 'Z') : -3, ('T', 'X') : -2, 
		('W', 'W') : 17, ('W', 'Y') : 2, ('W', 'V') : -5, ('W', 'B') : -9, 
		('W', 'Z') : -7, ('W', 'X') : -6, 
		('Y', 'Y') : 12, ('Y', 'V') : -5, ('Y', 'B') : -6, ('Y', 'Z') : -6, 
		('Y', 'X') : -4, 
		('V', 'V') : 8, ('V', 'B') : -7, ('V', 'Z') : -5, ('V', 'X') : -3, 
		('B', 'B') : 6, ('B', 'Z') : 0, ('B', 'X') : -4, 
		('Z', 'Z') : 6, ('Z', 'X') : -2, 
		('X', 'X') : -3
	}
}

def blosum_value(threshold, aa1, aa2):
	'''
	Returns the substitution value for two amino acids (order is
	unimportant because BLOSUM is symmetric).
	
	Raises KeyError if a substitution value for the two residues is
	not found.
	'''
	try:
		s = blosum[threshold][(aa1, aa2)]
	except KeyError:
		s = blosum[threshold][(aa2, aa1)]
	return s
