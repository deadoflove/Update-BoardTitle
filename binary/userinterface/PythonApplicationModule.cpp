// 1) Search: search at the end 

}

// 2) before its end make a new line and paste:

#ifdef ENABLE_UPDATE_BOARDTITLE
	PyModule_AddIntConstant(poModule, "UPDATE_BOARDTITLE", true);
#else
	PyModule_AddIntConstant(poModule, "UPDATE_BOARDTITLE", false);
#endif


// Example:

#ifdef ENABLE_UPDATE_BOARDTITLE
	PyModule_AddIntConstant(poModule, "UPDATE_BOARDTITLE", true);
#else
	PyModule_AddIntConstant(poModule, "UPDATE_BOARDTITLE", false);
#endif

}