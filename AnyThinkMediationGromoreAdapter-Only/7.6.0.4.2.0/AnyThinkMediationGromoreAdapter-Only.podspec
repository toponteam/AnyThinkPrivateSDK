#
# Be sure to run `pod lib lint TPNGromoreSDKAdapter-Only.podspec' to ensure this is a
# valid spec before submitting.
#
# Any lines starting with a # are optional, but their use is encouraged
# To learn more about a Podspec see https://guides.cocoapods.org/syntax/podspec.html
#

Pod::Spec.new do |s|
  s.name             = 'AnyThinkMediationGromoreAdapter-Only'
  s.version          = '7.6.0.4.2.0'
  s.summary          = 'AnyThinkGromoreSDKAdapter used for mediation with the TopOn SDK'

  s.description      = <<-DESC
     TopOn SDK for developer
                       DESC

  s.homepage = 'https://github.com/toponteam/AnyThinkPrivateSDK'
  s.author = { 'topon' => 'mct-js@toponad.com' }
  s.license = { :type => "MIT", :file => "AnyThinkGromoreAdapter-7.6.0.4.2.0/LICENSE" }

  s.ios.deployment_target = '11.0'
  s.static_framework = true
  s.requires_arc = true
  s.pod_target_xcconfig = {
    'OTHER_LDFLAGS' => ['-lObjC'],
    'VALID_ARCHS' => 'x86_64 armv7 armv7s arm64'
  }

  # s.source_files = 'AnyThinkGromoreAdapter/Classes/**/*'
  s.source = {
    :http => "http://topon-sdk-release.oss-cn-hangzhou.aliyuncs.com/AnyThink_Release/iosnetwork_2/AnyThinkGromoreAdapter/7.6.0.4.2.0/AnyThinkGromoreAdapter-7.6.0.4.2.0.zip",
    :type => 'zip'
  }
  s.vendored_frameworks = "AnyThinkGromoreAdapter-7.6.0.4.2.0/AnyThinkGromoreAdapter.xcframework"
  
  s.dependency 'AnyThinkiOS','>=6.5.60'

  s.dependency 'Ads-CN/BUAdSDK', '7.6.0.4'
  s.dependency 'Ads-CN/CSJMediation-Only', '7.6.0.4'
  
end
