#
# Be sure to run `pod lib lint TPNPangleAdapter.podspec' to ensure this is a
# valid spec before submitting.
#
# Any lines starting with a # are optional, but their use is encouraged
# To learn more about a Podspec see https://guides.cocoapods.org/syntax/podspec.html
#

Pod::Spec.new do |s|
  s.name             = 'TPNMediationPangleAdapter'
  s.version          = '7.9.1.1.0'
  s.summary          = 'TPNPangleAdapter used for mediation with the TopOn SDK'

  s.description      = <<-DESC
     TopOn SDK for developer
                       DESC

  s.homepage = 'https://github.com/CocoaPods/Specs/search?o=desc&q=TPNPangleAdapter&s=indexed'
  s.author = { 'topon' => 'mct-js@toponad.com' }
  s.license = { :type => "MIT", :file => "AnyThinkPangleAdapter-8.0.0.7.2/LICENSE" }

  s.ios.deployment_target = '12.0'
  s.static_framework = true
  s.requires_arc = true
  s.pod_target_xcconfig = {
    'OTHER_LDFLAGS' => ['-lObjC'],
    'VALID_ARCHS' => 'x86_64 armv7 armv7s arm64'
  }

  # s.source_files = 'TPNApplovinAdapter/Classes/**/*'
  s.source = {
    :http => "https://topon-sdk-release.oss-accelerate.aliyuncs.com/TPN_Release/iosnetwork/AnyThinkPangleAdapter/8.0.0.7.2/AnyThinkPangleAdapter-8.0.0.7.2.zip",
    :type => 'zip'
  }
  s.vendored_frameworks = "AnyThinkPangleAdapter-8.0.0.7.2/AnyThinkPangleAdapter.xcframework"
  s.dependency 'TPNiOS','>=6.4.94'
  s.dependency 'Ads-Global','7.9.1.1'
  
end
