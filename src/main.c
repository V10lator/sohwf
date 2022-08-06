#include <mocha/mocha.h>
#include <sysapp/launch.h>
#include <whb/proc.h>

int main()
{
	WHBProcInit();
	if(WHBProcIsRunning())
	{
		if(Mocha_InitLibrary() == MOCHA_RESULT_SUCCESS)
		{
			MochaRPXLoadInfo info = {
				.target = LOAD_RPX_TARGET_SD_CARD,
				.filesize = 0,
				.fileoffset = 0,
				.path = "wiiu/apps/soh/soh.rpx",
			};

			Mocha_LaunchRPX(&info);
			Mocha_DeinitLibrary();

		}
		else
			SYSLaunchMenu();

		while(WHBProcIsRunning()) {}
	}
//	WHBProcShutdown(); // TODO: Re-enable after HBL
	return 0;
}
