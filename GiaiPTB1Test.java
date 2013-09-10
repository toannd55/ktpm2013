package com;

import static org.junit.Assert.*;

import org.junit.Test;

public class GiaiPTB1Test {
	GiaiPTB1 test = new GiaiPTB1();
	
	@Test
	public void test() {
		assertEquals("Equals -1:", -1, test.PTB1(1, 1));
	}
	
	@Test
	public void test2(){
		assertEquals("Equals 9:", 9, test.PTB1(10, -90));
	}
}