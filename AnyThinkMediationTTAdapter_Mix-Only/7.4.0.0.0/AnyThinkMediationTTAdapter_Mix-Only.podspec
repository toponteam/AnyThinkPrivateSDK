#
# Be sure to run `pod lib lint AnyThinkTTAdapter_Mix-Only.podspec' to ensure this is a
# valid spec before submitting.
#
# Any lines starting with a # are optional, but their use is encouraged
# To learn more about a Podspec see https://guides.cocoapods.org/syntax/podspec.html
#

Pod::Spec.new do |s|
  s.name             = 'AnyThinkMediationTTAdapter_Mix-Only'
  s.version          = '7.4.0.0.0'
  s.summary          = 'AnyThinkTTAdapter_Mix used for mediation with the TopOn SDK'

  s.description      = <<-DESC
     TopOn SDK for developer
                       DESC
  
  s.homepage = 'https://github.com/toponteam/AnyThinkPrivateSDK'
  s.author = { 'topon' => 'mct-js@toponad.com' }
  s.license = { :type => "MIT", :file => "AnyThinkTTAdapter_Mix-7.4.0.0.0/LICENSE" }

  s.ios.deployment_target = '11.0'
  s.static_framework = true
  s.requires_arc = true
  s.pod_target_xcconfig = {
    'OTHER_LDFLAGS' => ['-lObjC'],
    'VALID_ARCHS' => 'x86_64 armv7 armv7s arm64'
  }

  # s.source_files = 'AnyThinkTTAdapter/Classes/**/*'
  s.source = {
    :http => "https://topon-sdk-release.oss-accelerate.aliyuncs.com/AnyThink_Release/iosnetwork/AnyThinkTTAdapter_Mix/7.4.0.0.0/AnyThinkTTAdapter_Mix-7.4.0.0.0.zip",
    :type => 'zip'
  }
  s.vendored_frameworks = "AnyThinkTTAdapter_Mix-7.4.0.0.0/AnyThinkTTAdapter_Mix.xcframework"
   
  s.dependency 'AnyThinkiOS','>=6.4.94'

  s.dependency 'Ads-CN-Beta/BUAdSDK', '7.4.0.0'
  s.dependency 'Ads-CN-Beta/CSJMediation-Only', '7.4.0.0'
  
end
