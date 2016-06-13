# android_report
项目中第三方库junit-report输出的文本为xml格式文本
这个脚本是用来解析这个xml文件的 暂时以print的方式输出，后续可能会支持html输出
使用方式：

    python android_report.py [输入xml路径] 

当然一般是持续集成到jenkins里面的

那么处理后的效果是这样的：

    ------------------------------------
    -->结果<-- 
    9 条通过 
    1 条失败
    成功率: 90.0 % 
    
    ------------------------------------
    失败用例:
    用例名: com.togic.TestLauncher.TestFav
    方法名: testCollection 
    日志:
    junit.framework.ComparisonFailure: expected:<[1]> but was:<[0]>
    	at junit.framework.Assert.assertEquals(Assert.java:85)
    	at junit.framework.Assert.assertEquals(Assert.java:91)
    	at com.togic.TestLauncher.TestFav.testCollection(TestFav.java:125)
    	at java.lang.reflect.Method.invokeNative(Native Method)
    	at java.lang.reflect.Method.invoke(Method.java:515)
    	at android.test.InstrumentationTestCase.runMethod(InstrumentationTestCase.java:220)
    	at android.test.InstrumentationTestCase.runTest(InstrumentationTestCase.java:205)
    	at android.test.ActivityInstrumentationTestCase2.runTest(ActivityInstrumentationTestCase2.java:202)
    	at junit.framework.TestCase.runBare(TestCase.java:134)
    	at junit.framework.TestResult$1.protect(TestResult.java:115)
    	at junit.framework.TestResult.runProtected(TestResult.java:133)
    	at junit.framework.TestResult.run(TestResult.java:118)
    	at junit.framework.TestCase.run(TestCase.java:124)
    	at android.test.AndroidTestRunner.runTest(AndroidTestRunner.java:203)
    	at android.test.AndroidTestRunner.runTest(AndroidTestRunner.java:177)
    	at android.test.InstrumentationTestRunner.onStart(InstrumentationTestRunner.java:554)
    	at android.app.Instrumentation$InstrumentationThread.run(Instrumentation.java:1715)
    --
    ------------------------------------
    成功用例:
    用例名: com.togic.TestLauncher.TestLauncherMove
    方法名: testAllMove   执行时间: 25.233
    --
    用例名: com.togic.TestLauncher.TestFav
    方法名: testAddData   执行时间: 14.999
    方法名: testClick   执行时间: 12.460
    方法名: testDelete   执行时间: 9.960
    --
    用例名: com.togic.TestProgramInfo.TestProgramInfo02
    方法名: testMovie   执行时间: 70.153
    --
    用例名: com.togic.TestLauncher.TestSearch
    方法名: testCleanButton   执行时间: 14.293
    方法名: testLastWorld   执行时间: 12.402
    方法名: testMultSoll   执行时间: 19.661
    方法名: testSearch   执行时间: 17.095
    --
    ------------------------------------
提取出了错误日志，这样后续处理会方便得多。
